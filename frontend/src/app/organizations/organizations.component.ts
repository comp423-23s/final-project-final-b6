import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from 'src/app/organizations/gate.guard';
import { Organization, OrganizationService } from './organizations.service';
import { PermissionService } from '../permission.service';
import { MatDialog } from '@angular/material/dialog';
import { DeleteDialogComponent } from './delete-dialog/delete-dialog.component';


@Component({
  selector: 'app-organizations',
  templateUrl: './organizations.component.html',
  styleUrls: ['./organizations.component.css']
})
export class OrganizationsComponent {
  static Route: Route = {
    path: 'organizations',
    component: OrganizationsComponent, 
    title: 'Organizations', 
  };
  public organizations$: Observable<Organization[]>;
  public adminPermission$: Observable<boolean>;
  public organizationPermission$: Observable<boolean>;
  constructor(
    private permission: PermissionService,
    private organizationService: OrganizationService,
    protected deleteDialog: MatDialog
  ) {
    this.organizations$=organizationService.getOrganizations();
    this.adminPermission$ = this.permission.check('admin.view', 'admin/')
    this.organizationPermission$ = this.permission.check('organization.edit_organization', 'organizations/')
  }
  deleteOrganization(organization: Organization) {
    let dialogRef = this.deleteDialog.open(DeleteDialogComponent, { data: { "organization": organization} });
    dialogRef.afterClosed().subscribe(() => { this.organizations$=this.organizationService.getOrganizations();})
  }

}
