import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
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
    title: '',
    description: '',
    mission: '',
    photoUrl: ''});


  constructor(
    private organizationservice: OrganizationService,
    private formBuilder: FormBuilder,
    ) {}

  onSubmit(): void {
    let form = this.form.value;
    let id = 0;
    let name = form.title ?? "";
    let overview = form.description ?? "";
    let description = form.mission ?? "";
    let image = form.photoUrl ?? "" ;
    console.log("eh")
    
    this.organizationservice
      .createOrganization(id,name,overview,description,image)
      .subscribe({
        next: (organization) => this.onSuccess(organization),
        error: (err) => this.onError(err)
      });
    };
    

    private onSuccess(organization: Organization):void {
      console.log('d');
      window.alert("Success")
      this.form.reset();
    }
    private onError(err: HttpErrorResponse | Error) {
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