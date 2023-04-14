import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Event, EventService } from "../event-service";


@Component({
  selector: 'app-delete-dialog-event',
  templateUrl: './delete-dialog-event.component.html',
  styleUrls: []
})
export class DeleteDialogEventComponent implements OnInit {

  constructor(private eventService: EventService,
    private dialogRef: MatDialogRef<DeleteDialogEventComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { event: Event }
  ) { }

  ngOnInit(): void { }
  deleteEvent(event: Event) {
    this.eventService.deleteEvent(event.id);
    this.dialogRef.close();
  }

}