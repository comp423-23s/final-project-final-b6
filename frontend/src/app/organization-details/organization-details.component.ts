import { Component } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { OrganizationService } from '../organizations/organizations.service';
import { OrganizationDetailsService, Event } from './organization-details.service';
import { Organization } from '../organizations/organizations.service';
import {FormControl} from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-organization-details',
  templateUrl: './organization-details.component.html',
  styleUrls: ['./organization-details.component.css']
})
export class OrganizationDetailsComponent {
  fontStyleControl = new FormControl('');
  tab?: string;

  public organization$: Observable<Organization>;

  public events$: Observable<Event[]>;

  static Route: Route = {
    path: 'organizations/:organizationName',
    component: OrganizationDetailsComponent, 
    title: 'Organization Details', 
  };
  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private organizationDetailsService: OrganizationDetailsService) { 
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
      // set the default tab to the details/registration page
      this.tab = "Details/Registration";
      // call API route to get events for organization
      this.events$ = this.organizationDetailsService.getOrganizationEvents(String(routeParams.get('organizationName')));
    }



}
