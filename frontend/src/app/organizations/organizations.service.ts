import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';
import { ReturnStatement } from '@angular/compiler';

export interface Organization {
  id: number;
  name: string;
  overview: string;
  description: string;
  image: string;
}

@Injectable({
  providedIn: 'root'
})
export class OrganizationService {
  apiBaseUrl = "/api";
  organizations: Organization[] = [];

  constructor(private http: HttpClient) { }

  getOrganizations() : Observable<Organization[]> {
    return this.http.get<Organization[]>("/api/organizations");
  }

  getOrganizationDetails(organizationName: string): Observable<Organization>{
    return this.http.get<Organization>(`api/organizations/${organizationName}`)
  }

  deleteOrganization(organization: Organization) {
    return this.http.delete<Organization>(`/api/organizations/${organization.name}`);
  }

  editOrganization(organization: Organization): Observable<Organization>{
    const body = {
        id: organization.id,
        name: organization.name,
        overview: organization.overview,
        description: organization.description,
        image: organization.image
      }
    return this.http.patch<Organization>(`/api/organizations/${organization.name}`, body);
  }

  createOrganization(id: number, name: string, overview: string, description: string, image: string): Observable<Organization> {
    let errors: string[] = [];
    if (name === "") {
      errors.push(`name required.`);
    }

    if (overview === "") {
      errors.push(`overview required.`)
    }

    if (description === "") {
      errors.push(`description required.`)
    }

    if (image === "") {
      errors.push(`image required.`)
    }

    if (errors.length > 0) {
      return throwError(() => { return new Error(errors.join("\n")) });
    }

    let organization: Organization = {id, name, overview, description, image};
    return this.http.post<Organization>('/api/organizations', organization);
  }
}


