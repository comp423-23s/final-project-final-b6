import { Component } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { FormBuilder } from '@angular/forms';
import { OrganizationService, Organization } from '../organizations/organizations.service';

@Component({
  selector: 'app-add-club-form',
  templateUrl: './add-club-form.component.html',
  styleUrls: ['./add-club-form.component.css']
})
export class AddClubFormComponent {
  form = this.formBuilder.group({
    id: 0,
    name: '',
    overview: '',
    description: '',
    image: ''
  });

  constructor(
    private organizationservice: OrganizationService,
    private formBuilder: FormBuilder,
  ) {}

  onSubmit(): void {
    this.organizationservice
      .getOrganizations()
      .subscribe({
        next: (organizations) => {
          const id = organizations.length > 0 ? Math.max(...organizations.map(o => o.id)) + 1 : 0;
          const form = this.form.value;
          const name = form.name ?? "";
          const overview = form.overview ?? "";
          const description = form.description ?? "";
          const image = form.image ?? "";
  
          console.log("working!");
          console.log("onsubmit!");
          console.log(id);
          console.log("name");
          console.log(name); // Add this line to check the value of `name`
  
          this.organizationservice
            .createOrganization(id, name, overview, description, image)
            .subscribe({
              next: (organization) => this.onSuccess(organization),
              error: (err) => this.onError(err)
            });
        },
        error: (err) => this.onError(err)
      });
  }
  
  
  private onSuccess(organization: Organization): void {
    console.log("succcccc!");
    window.alert("Success");
    this.form.reset();
  }

  private onError(err: HttpErrorResponse | Error) {
    console.log("errorrrr");
    if (err instanceof HttpErrorResponse) {
      if (err.message) {
        window.alert(err.error.detail);
      } else {
        window.alert("Unknown HTTP error: " + JSON.stringify(err));
      }
    } else {
      window.alert(err);
    }
  }
}
