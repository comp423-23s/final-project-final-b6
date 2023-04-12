import { Component } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { EventService, Event } from './event-service';
import { OrganizationService } from 'src/app/organizations/organizations.service';
import { Organization } from 'src/app/organizations/organizations.service';
import { PermissionService } from 'src/app/permission.service';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})

export class EventsComponent {
  public organization$: Observable<Organization>;

  public events$: Observable<Event[]>;

  public adminPermission$: Observable<boolean>;


  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private permission: PermissionService,
    private eventService: EventService) { 
      this.adminPermission$ = this.permission.check('admin.view', 'admin/')
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
      // call API route to get events for organization
      this.events$ = this.eventService.getOrganizationEvents(String(routeParams.get('organizationName')));
    }
  }