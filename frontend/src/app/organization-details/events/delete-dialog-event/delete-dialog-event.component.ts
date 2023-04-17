import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Event, EventService } from "../event-service";
import { Organization } from 'src/app/organizations/organizations.service';


@Component({
  selector: 'app-delete-dialog-event',
  templateUrl: './delete-dialog-event.component.html',
  styleUrls: []
})
export class DeleteDialogEventComponent implements OnInit {

  constructor(private eventService: EventService,
    private dialogRef: MatDialogRef<DeleteDialogEventComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { organization:Organization, event: Event }
  ) { }

  ngOnInit(): void { }
  deleteEvent( organization:Organization,event: Event) {
    this.eventService.deleteEvent(organization.name,event.id).subscribe(()=>{
      this.dialogRef.close();
    });
  }

}