# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=213ms, nekobox=261ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=232ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=231ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=199ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=230ms, nekobox=281ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=210ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=279ms, nekobox=7178ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=213ms, nekobox=7177ms, status=no)
9. `AKUN-007-WPENG-VLESS-WS-96MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-84MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-ORG-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CCWU-VLESS-WS-90MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-120MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-107MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-120MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-113MS` (url=208ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-150MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-86MS` (url=212ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-77MS` (url=229ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-101MS` (url=277ms, status=HTTP 204)
25. `AKUN-025-NEXUSMODS-VLESS-WS-135MS` (url=233ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
