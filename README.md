#nobleep api

## endpoints

# ```GET /job/read```
_Gets all of the jobs_

returns 
```json
{

  "jobs": [

    {

      "acknowledged": null,

      "bed": "bed",

      "created_at": "Sat, 14 May 2016 17:56:06 GMT",

      "creator_comment": "creator_comment",

      "creator_id": null,

      "creator_name": "creator_name",

      "doctor_comment": "doctor_comment",

      "done": null,

      "id": 1,

      "location": "location",

      "patient_id": "patient_id",

      "team_id": 1,

      "urgency": 1,

      "ward": "ward"

    }
  ]
}
```

# ```GET /job/read/<team_id>```
_Gets all the jobs for a team_id_

returns same as above

# ```POST /job/create```
_Creates a job_

__team_id__

__patient_id__

__urgency__

__creator_comment__

__doctor_comment__

__bed__

__ward__

__location__

__creator_name__

# ```POST /job/update/<id>```
_Updates the job with id_

__team_id__ _optional_

__patient_id__ _optional_

__urgency__ _optional_

__creator_comment__ _optional_

__doctor_comment__ _optional_

__bed__ _optional_

__ward__ _optional_

__location__ _optional_

__creator_name__ _optional_

__acknowledged__ _optional_

__done__ _optional_
