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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=217ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-67MS` (url=238ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=235ms, nekobox=249ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-86MS` (url=220ms, nekobox=250ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-86MS` (url=220ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=235ms, nekobox=261ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-73MS` (url=231ms, nekobox=188ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-122MS`
11. `AKUN-010-ZVC-VLESS-WS-131MS`
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-133MS` (url=254ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-137MS` (url=244ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-123MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-74MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-ES-FORNEX-20160629-VLESS-WS-111MS` (url=243ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-MICROSOFT-VLESS-WS-347MS` (url=743ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-359MS` (url=748ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-355MS` (url=764ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-238MS` (url=537ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-355MS` (url=835ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-404MS` (url=820ms, status=HTTP 204)
24. `AKUN-025-DEV-VLESS-WS-559MS` (url=674ms, status=HTTP 204)
25. `AKUN-027-SPEEDTEST-VLESS-WS-640MS` (url=748ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
