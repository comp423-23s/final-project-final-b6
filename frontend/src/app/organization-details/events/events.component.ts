import { Component } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { EventService, Event } from './event-service';
import { OrganizationService } from 'src/app/organizations/organizations.service';
import { Organization } from 'src/app/organizations/organizations.service';
import {FormControl} from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})

export class EventsComponent {
  public organization$: Observable<Organization>;

  public events$: Observable<Event[]>;

  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private eventService: EventService) { 
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
      // call API route to get events for organization
      this.events$ = this.eventService.getOrganizationEvents(String(routeParams.get('organizationName')));
    }
  }

