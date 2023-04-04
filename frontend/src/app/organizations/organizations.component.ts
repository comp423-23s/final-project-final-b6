import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from 'src/app/organizations/gate.guard';
import { Organization, OrganizationService } from './organizations.service';

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
  
  constructor(
    private organizationService: OrganizationService
  ) {
    this.organizations$=organizationService.getOrganizations()
  }
}
