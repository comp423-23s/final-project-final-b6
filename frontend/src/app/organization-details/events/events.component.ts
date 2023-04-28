import { Component } from '@angular/core';
import { ActivatedRoute} from '@angular/router';
import { Observable } from 'rxjs';
import { EventService, Event } from './event-service';
import { OrganizationService } from 'src/app/organizations/organizations.service';
import { Organization } from 'src/app/organizations/organizations.service';
import { PermissionService } from 'src/app/permission.service';
import { DeleteDialogEventComponent } from './delete-dialog-event/delete-dialog-event.component'
import { MatDialog } from '@angular/material/dialog';


@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})

export class EventsComponent {
  public organization$: Observable<Organization>;

  public events$: Observable<Event[]>;

  public adminPermission$: Observable<boolean>;

  public eventPermission$: Observable<boolean>;
  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private permission: PermissionService,
    protected deleteDialog: MatDialog,
    private eventService: EventService) { 
      // get admin permission to check if triple dot should be rendered (we probably need to change this later when we do more authentication stuff)
      this.adminPermission$ = this.permission.check('admin.view', 'admin/')
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
      // call API route to get events for organization
      this.events$ = this.eventService.getOrganizationEvents(String(routeParams.get('organizationName')));
      let orgName = String(routeParams.get('organizationName'));
      this.eventPermission$ = this.permission.check('event.edit_event', `organizations/${orgName}`)
    }

    deleteEvent(organization: Organization,event: Event) {
      let dialogRef = this.deleteDialog.open(DeleteDialogEventComponent, { data: {"organization":organization, "event": event} });
      dialogRef.afterClosed().subscribe(() => {
        this.events$ = this.eventService.getOrganizationEvents(String(this.route.snapshot.paramMap.get('organizationName')));
      })
    }
  }