import { Component } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { OrganizationService } from '../organizations/organizations.service';
import { Organization } from '../organizations/organizations.service';
@Component({
  selector: 'app-organization-details',
  templateUrl: './organization-details.component.html',
  styleUrls: ['./organization-details.component.css']
})
export class OrganizationDetailsComponent {
  public organization$: Observable<Organization>;

  static Route: Route = {
    path: 'organizations/:organizationName',
    component: OrganizationDetailsComponent, 
    title: 'Organization Details', 
  };
  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute) { 
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganization(String(routeParams.get('organizationName')))
    }

}
