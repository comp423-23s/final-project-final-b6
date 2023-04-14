import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

/* HTTP and Auth */
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpRequestInterceptor } from './navigation/http-request.interceptor';
import { JwtModule } from '@auth0/angular-jwt';

/* UI / Material Dependencies */
import { NgForOf } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { LayoutModule } from '@angular/cdk/layout';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatSliderModule } from '@angular/material/slider';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule} from '@angular/material/menu';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import { NgModel } from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';

/* Application Specific */
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationComponent } from './navigation/navigation.component';
import { ErrorDialogComponent } from './navigation/error-dialog/error-dialog.component';
import { HomeComponent } from './home/home.component';
import { GateComponent } from './gate/gate.component';
import { ProfileEditorComponent } from './profile/profile-editor/profile-editor.component';
import { OrganizationsComponent } from './organizations/organizations.component';
import { OrganizationDetailsComponent } from './organization-details/organization-details.component';
import { DeleteDialogComponent } from './organizations/delete-dialog/delete-dialog.component';
import { FormsModule } from '@angular/forms';
import { EventsComponent } from './organization-details/events/events.component';
import { DetailsAndRegistrationComponent } from './organization-details/details-and-registration/details-and-registration.component';
import { MembersComponent } from './organization-details/members/members.component';
import { EventEditComponent } from './organization-details/events/event-edit/event-edit.component';
import { MatSelectModule } from '@angular/material/select';
import { DeleteDialogEventComponent } from './organization-details/events/delete-dialog-event/delete-dialog-event.component';
import { OrganizationEditComponent } from './organization-edit/organization-edit.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    ErrorDialogComponent,
    HomeComponent,
    GateComponent,
    ProfileEditorComponent,
    OrganizationsComponent,
    OrganizationDetailsComponent,
    DeleteDialogComponent,
    EventsComponent,
    DetailsAndRegistrationComponent,
    MembersComponent,
    DeleteDialogEventComponent,
    EventEditComponent,
    OrganizationEditComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    NgForOf,
    AppRoutingModule,
    LayoutModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatDialogModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatProgressBarModule,
    MatSidenavModule,
    MatSliderModule,
    MatSnackBarModule,
    MatTabsModule,
    MatToolbarModule,
    MatMenuModule,
    MatTableModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatSelectModule,
    FormsModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          return localStorage.getItem("bearerToken")
        }
      }
    }),
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: HttpRequestInterceptor,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule {}