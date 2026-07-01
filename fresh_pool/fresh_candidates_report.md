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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=213ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=215ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, nekobox=192ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS`
5. `AKUN-004-COMPREND-NET-VLESS-WS-73MS`
6. `AKUN-005-ZVC-VLESS-WS-73MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS`
9. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-85MS`
10. `AKUN-009-COMPREND-NET-VLESS-WS-81MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-79MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-94MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-86MS` (url=197ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-95MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-117MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-97MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-84MS` (url=214ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-165MS` (url=301ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-348MS` (url=746ms, status=HTTP 204)
22. `AKUN-024-MICROSOFT-VLESS-WS-358MS` (url=835ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-382MS` (url=830ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-369MS` (url=823ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-383MS` (url=813ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
