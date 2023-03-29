import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from 'src/app/gate/gate.guard';
import { Organizations, OrganizationsService } from '../organizations.service';

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
  public organizations$: Observable<Organizations[]>;

  
  constructor(
    private organizationService: OrganizationsService
  ) {
    this.organizations$=organizationService.getOrganizations()
  }

}


