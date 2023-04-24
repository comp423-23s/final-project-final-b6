import { Component } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { FormBuilder } from '@angular/forms';
import { Event, EventService } from "../event-service";
import { Organization, OrganizationService } from 'src/app/organizations/organizations.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { isAuthenticated } from '../../../organizations/gate.guard'

@Component({
  selector: 'app-event-create',
  templateUrl: './event-create.component.html',
  styleUrls: ['./event-create.component.css']
})
// Component responsible for handling rendering of event creating
export class EventCreateComponent {
  static Route: Route = {
    path: 'organizations/:organizationName/events/create',
    component: EventCreateComponent,
    title: 'Create Event',
    canActivate: [isAuthenticated]
  };
  public organization$: Observable<Organization>;
  // need to store date time information as member variables to parse input
  public selectedHourValue: string;
  public selectedMinuteValue: string;
  public selectedAmPmValue: string;
  public hours: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];
  public minutes: string[] = ['00', '15', '30', '45'];
  public timeOfDay: string[] = ['AM', 'PM'];
  public organizationID: number;
  public organizationName: string;
  public eventCreateForm = this.formBuilder.group({
    name: '',
    description: '',
    date: new Date(''),
    location: '',
    image: ''
  })
  constructor(
    private eventService: EventService,
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    protected formBuilder: FormBuilder,
    protected snackBar: MatSnackBar,
    private router: Router) {
    const form = this.eventCreateForm;
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
    this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
    this.organizationID = 0;
    this.organizationName = String(routeParams.get('organizationName'));
    // default vals for hours, minutes, and AM/PM
    this.selectedHourValue = '';
    this.selectedMinuteValue = '';
    this.selectedAmPmValue = '';
  }

  ngOnInit(): void {
    this.organization$.subscribe(
      (organization) => {
        this.organizationID = organization.id;
        this.organizationName = organization.name;
      }
    )
  }

  onSubmit(): void {

    // get all the updated info
    let updatedName = this.eventCreateForm.get("name")?.value ?? "";
    let updatedDescription = this.eventCreateForm.get("description")?.value ?? "";
    let updatedLocation = this.eventCreateForm.get("location")?.value ?? "";
    let updatedImage = this.eventCreateForm.get("image")?.value ?? "";
    let updatedDateRaw = this.eventCreateForm.get("date")?.value ?? new Date("");
    // deal with time conversions
    // func returns the corrected hours
    let hours24 = this.convertHours12to24(this.selectedHourValue, this.selectedAmPmValue);
    var updatedDate = new Date(updatedDateRaw.getUTCFullYear(), updatedDateRaw.getMonth(), updatedDateRaw.getDate(), parseInt(hours24) - 4, parseInt(this.selectedMinuteValue));
    // create event object with all the new updated information
    let updatedEvent: Event = {
      id: 0,
      name: updatedName,
      description: updatedDescription,
      date_time: updatedDate,
      location: updatedLocation,
      image: updatedImage,
      organization_id: this.organizationID
    }
    // call the update API endpoint to update the event
    this.eventService.createEvent(this.organizationName, updatedEvent).subscribe(
      (event) => { this.onSuccess(event) }
    );
  }

  private onSuccess(event: Event) {
    this.snackBar.open("Event Created", "", { duration: 2000 });
    this.router.navigate([`/organizations/${this.organizationName}`]);
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
  onReturn() {
    this.router.navigate([`/organizations/${this.organizationName}`])
    }
}
