import { Component } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { FormBuilder} from '@angular/forms';
import { Event, EventService } from "../event-service";
import { MatSnackBar } from '@angular/material/snack-bar';
import { isAuthenticated } from '../../../organizations/gate.guard'

@Component({
  selector: 'app-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})

export class EventEditComponent {
  public event$: Observable<Event>;
  public selectedHourValue: string;
  public selectedMinuteValue: string;
  public selectedAmPmValue: string;
  public hours: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];
  public minutes: string[] = ['00', '15', '30', '45'];
  public timeOfDay: string[] = ['AM', 'PM'];
  public eventID: number;
  public organizationID: number;
  public organizationName: string;
  public eventEditForm = this.formBuilder.group({
    name: '',
    description: '',
    date: new Date(''),
    location: '',
    image: ''
  })
  static Route: Route = {
    path: 'organizations/:organizationName/events/:eventID/edit',
    component: EventEditComponent,
    title: 'Event Edit',
    canActivate: [isAuthenticated]
  };
  constructor(
    private eventService: EventService,
    private route: ActivatedRoute,
    protected formBuilder: FormBuilder,
    protected snackBar: MatSnackBar) {
    const form = this.eventEditForm;
    form.get('name');
    form.get('description');
    form.get('date');
    form.get('time');
    form.get('AmPm');
    form.get('location');
    form.get('image');
    // First get organization name from the current route.
    const routeParams = this.route.snapshot.paramMap;
    // call API route to get specific info of organization
    this.event$ = this.eventService.getEvent(String(routeParams.get('organizationName')), Number(routeParams.get('eventID')));
    this.organizationID = 0;
    this.eventID = 0;
    this.organizationName = String(routeParams.get('organizationName'));
    // default vals for hours, minutes, and AM/PM
    this.selectedHourValue = '';
    this.selectedMinuteValue = '';
    this.selectedAmPmValue = '';
  }

  ngOnInit(): void {
    this.event$.subscribe(
      (event) => {
        let eventDate = new Date(event.date_time)
        this.eventID = event.id;
        this.selectedHourValue = (eventDate.getHours().toString() == '0' ? '12' : eventDate.getHours().toString());
        // account for date time being in 24 hour time
        this.selectedHourValue = parseInt(this.selectedHourValue) > 12 ? String(parseInt(this.selectedHourValue) - 12) : this.selectedHourValue;
        this.selectedMinuteValue = (eventDate.getMinutes().toString() == '0' ? '00' : eventDate.getMinutes().toString());
        this.selectedAmPmValue = (eventDate.getHours() >= 12 ? 'PM' : 'AM');
        this.organizationID = event.organization_id;
        this.eventEditForm.setValue({
          name: event.name,
          description: event.description,
          date: eventDate,
          location: event.location,
          image: event.image
        })
      }
    )
  }

  onSubmit(): void {

    // get all the updated info
    let updatedName = this.eventEditForm.get("name")?.value ?? "";
    let updatedDescription = this.eventEditForm.get("description")?.value ?? "";
    let updatedLocation = this.eventEditForm.get("location")?.value ?? "";
    let updatedImage = this.eventEditForm.get("image")?.value ?? "";
    let updatedDateRaw = this.eventEditForm.get("date")?.value ?? new Date("");
    // deal with time conversions
    // func returns the corrected hours
    let hours24 = this.convertHours12to24(this.selectedHourValue, this.selectedAmPmValue);
    var updatedDate = new Date(updatedDateRaw.getUTCFullYear(), updatedDateRaw.getMonth(), updatedDateRaw.getDate(), parseInt(hours24) - 4, parseInt(this.selectedMinuteValue));
    console.log(updatedDate);
    // create event object with all the new updated information
    let updatedEvent: Event = {
      id: this.eventID,
      name: updatedName,
      description: updatedDescription,
      date_time: updatedDate,
      location: updatedLocation,
      image: updatedImage,
      organization_id: this.organizationID
    }
    // call the update API endpoint to update the event
    this.eventService.editEvent(this.organizationName, updatedEvent).subscribe(
      (event) => { this.onSuccess(event) }
    );
  }

  private onSuccess(event: Event) {
    this.snackBar.open("Event Saved", "", { duration: 2000 })
  }

  public changeClientMinute(minute: string) {
    this.selectedMinuteValue = minute;
  }
  public changeClientHour(hour: string) {
    this.selectedHourValue = hour;
  }
  public changeClientAmPm(AmPm: string) {
    this.selectedAmPmValue = AmPm;
  }
  public convertHours12to24(hours: string, AmPm: string) {
    if (hours === "12") {
      hours = "00";
    }
    if (AmPm === "PM") {
      hours = String(parseInt(hours, 10) + 12);
    }
    return hours
  };
}