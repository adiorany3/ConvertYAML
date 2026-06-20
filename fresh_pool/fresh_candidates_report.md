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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=194ms, nekobox=179ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=193ms, nekobox=177ms, status=no)
4. `AKUN-004-DEV-VLESS-WS-75MS` (url=189ms, nekobox=202ms, status=no)
5. `AKUN-002-UNKNOWN-VLESS-WS-70MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=190ms, nekobox=179ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=192ms, nekobox=180ms, status=no)
8. `AKUN-003-UNKNOWN-VLESS-WS-83MS`
9. `AKUN-004-UNKNOWN-VLESS-WS-92MS`
10. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS`
11. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS`
12. `AKUN-007-UNKNOWN-VLESS-WS-108MS`
13. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS`
14. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-354MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-393MS` (url=829ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-392MS` (url=852ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-390MS` (url=885ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-411MS` (url=812ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-619MS` (url=874ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-627MS` (url=890ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-631MS` (url=876ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-344MS` (url=748ms, status=HTTP 204)
24. `AKUN-027-BROADNNET-KR-VLESS-WS-641MS` (url=968ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-681MS` (url=1418ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
