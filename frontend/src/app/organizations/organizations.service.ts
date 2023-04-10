import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
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
    console.log(organization);
    const index = this.organizations.indexOf(organization);
    if (index >= 0) {
      this.organizations.splice(index, 1);
    }
  }
}


