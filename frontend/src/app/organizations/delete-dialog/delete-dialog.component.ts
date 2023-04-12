import { Component, Inject, OnInit } from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
import { Organization, OrganizationService } from '../organizations.service';


@Component({
  selector: 'app-delete-dialog',
  templateUrl: './delete-dialog.component.html',
  styleUrls: []
})
export class DeleteDialogComponent implements OnInit {

  constructor(private organizationService: OrganizationService, 
    private dialogRef: MatDialogRef<DeleteDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: {organization: Organization}
  ) {}

  ngOnInit(): void {}
  deleteOrganization(organization: Organization){
    this.organizationService.deleteOrganization(organization);
    this.dialogRef.close();
  }

}