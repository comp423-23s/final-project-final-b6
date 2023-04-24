import { Component } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { FormBuilder, Validators } from '@angular/forms';
import { OrganizationService } from '../organizations/organizations.service';
import { Organization } from '../organizations/organizations.service';
import { FormControl } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { isAuthenticated } from '../organizations/gate.guard';

@Component({
  selector: 'app-organization-edit',
  templateUrl: './organization-edit.component.html',
  styleUrls: ['./organization-edit.component.css']
})
export class OrganizationEditComponent {
  public organization$: Observable<Organization>;
  public organizationName: String;
  public organizationID: number;
  public organizationEditForm = this.formBuilder.group({
    overview: '',
    description: '',
    image: ''
  })
  static Route: Route = {
    path: 'organizations/:organizationName/edit',
    component: OrganizationEditComponent,
    title: 'Edit Organization',
    canActivate: [isAuthenticated]
  };
  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    protected formBuilder: FormBuilder,
    protected snackBar: MatSnackBar,
    private router: Router) {
    const form = this.organizationEditForm;
    form.get('overview');
    form.get('description');
    form.get('image');
    // First get organization name from the current route.
    const routeParams = this.route.snapshot.paramMap;
    // call API route to get specific info of organization
    this.organization$ = this.organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
    this.organizationName = ''
    this.organizationID = 0;
  }

  ngOnInit(): void {
    this.organization$.subscribe(
      (organization) => {
        this.organizationName = organization.name;
        this.organizationID = organization.id;
        this.organizationEditForm.setValue({
          overview: organization.overview,
          description: organization.description,
          image: organization.image
        })
      }
    )
  }

  onSubmit(): void {
    // get all the updated info
    let updatedOverview = this.organizationEditForm.get("overview")?.value ?? "";
    let updatedDescription = this.organizationEditForm.get("description")?.value ?? "";
    let updatedImage = this.organizationEditForm.get("image")?.value ?? "";
    let updatedOrganization: Organization = {
      id: this.organizationID, name: this.organizationName.toString(),
      overview: updatedOverview,
      description: updatedDescription,
      image: updatedImage
    }
    // call the update API endpoint
    this.organizationService.editOrganization(updatedOrganization).subscribe(
      (organization) => { this.onSuccess(organization) }
    );
  }
  private onSuccess(organization: Organization) {
    this.snackBar.open("Organization Saved", "", { duration: 2000 })
    this.router.navigate(['/organizations']);
  }
  onReturn(): void {
    this.router.navigate(['/organizations']);
  }
}
