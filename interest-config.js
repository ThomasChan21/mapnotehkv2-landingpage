/**
 * MapNoteHK interest form configuration.
 *
 * Where submissions go:
 * - FORM_ENDPOINT set → POST JSON to that URL (Formspree, Tally webhook, or your API).
 * - FORM_ENDPOINT empty → saved only in the visitor's browser localStorage (preview/dev).
 *
 * Production uses Formspree so interest registrations are emailed to the site owner.
 */
window.MapNoteInterestConfig = {
  /**
   * Formspree endpoint for the interest registration form.
   * Submissions POST JSON with name, email, role, district, interests, and metadata.
   */
  FORM_ENDPOINT: 'https://formspree.io/f/xykrjqlk',
  /** localStorage key when FORM_ENDPOINT is not set */
  STORAGE_KEY: 'mapnotehk_interest_submissions',
};
