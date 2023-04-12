import { Component } from '@angular/core';
import { ActivatedRoute} from '@angular/router';
import { Observable } from 'rxjs';
import { OrganizationService } from 'src/app/organizations/organizations.service';
import { Organization } from 'src/app/organizations/organizations.service';

@Component({
  selector: 'app-details-and-registration',
  templateUrl: './details-and-registration.component.html',
  styleUrls: ['./details-and-registration.component.css']
})

export class DetailsAndRegistrationComponent {
  public organization$: Observable<Organization>;

  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,) { 
      // First get organization name from the current route.
      const routeParams = this.route.snapshot.paramMap;
      // call API route to get specific info of organization
      this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
    }
}
