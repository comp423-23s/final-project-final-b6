import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from 'src/app/organizations/gate.guard';
import { Organization, OrganizationService } from './organizations.service';
import { PermissionService } from '../permission.service';



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
  
  constructor(
    private permission: PermissionService,
    private organizationService: OrganizationService
  ) {
    this.organizations$=organizationService.getOrganizations()
    this.adminPermission$ = this.permission.check('admin.view', 'admin/')
  }
  deleteOrganization(organization: Organization) {
    if (confirm('Are you sure you want to delete?')) {
      this.organizationService.deleteOrganization(organization);
    }
  }
}

