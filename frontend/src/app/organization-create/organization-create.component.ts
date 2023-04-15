import { Component } from '@angular/core';
import { ActivatedRoute, Route, Router, RouteConfigLoadEnd } from '@angular/router';
import { Observable } from 'rxjs';
import { FormBuilder, Validators } from '@angular/forms';
import { OrganizationService } from '../organizations/organizations.service';
import { Organization } from '../organizations/organizations.service';
import { FormControl } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { isAuthenticated } from '../organizations/gate.guard';

@Component({
  selector: 'app-organization-create',
  templateUrl: './organization-create.component.html',
  styleUrls: ['./organization-create.component.css']
})
export class OrganizationCreateComponent {
  public organizationCreateForm = this.formBuilder.group({
    name: '',
    overview: '',
    description: '',
    image: ''
  })
  static Route: Route = {
    path: 'create/organization',
    component: OrganizationCreateComponent,
    title: 'Create Organization',
    canActivate: [isAuthenticated]
  };
  constructor(
    private organizationService: OrganizationService,
    protected formBuilder: FormBuilder,
    protected snackBar: MatSnackBar,
    private router: Router) {
    const form = this.organizationCreateForm;
    form.get('overview');
    form.get('description');
    form.get('image');
  }


  onSubmit(): void {
    // get all the updated info
    let name = this.organizationCreateForm.get("name")?.value ?? "";
    let overview = this.organizationCreateForm.get("overview")?.value ?? "";
    let description = this.organizationCreateForm.get("description")?.value ?? "";
    let image = this.organizationCreateForm.get("image")?.value ?? "";
    let id = 0;
    // call the update API endpoint
    this.organizationService.createOrganization(id, name, overview, description, image).subscribe(
      (organization) => { this.onSuccess(organization) }
    );
  }
  private onSuccess(organization: Organization) {
    console.log("wooooooooo");
    this.snackBar.open("Organization Created", "", { duration: 2000 });
    this.router.navigate(['/organizations']);
  }
}

