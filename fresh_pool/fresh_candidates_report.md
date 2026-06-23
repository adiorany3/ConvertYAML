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
1. `AKUN-001-090227-VLESS-WS-66MS` (url=221ms, nekobox=241ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=226ms, nekobox=234ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS` (url=225ms, nekobox=249ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=216ms, nekobox=176ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-117MS` (url=238ms, nekobox=190ms, status=no)
6. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-113MS`
8. `AKUN-008-DEV-VLESS-WS-137MS` (url=290ms, nekobox=177ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-108MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=257ms, nekobox=198ms, status=no)
11. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS`
12. `AKUN-008-UNKNOWN-VLESS-WS-149MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-94MS` (url=198ms, nekobox=247ms, status=no)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=241ms, nekobox=224ms, status=no)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-89MS` (url=251ms, nekobox=210ms, status=no)
16. `AKUN-009-CLOUDFLARE-VLESS-WS-230MS`
17. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-278MS`
18. `AKUN-018-CLOUDFLARE-VLESS-WS-279MS` (url=583ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-278MS` (url=584ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-286MS` (url=700ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-141MS` (url=250ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-281MS` (url=501ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-267MS` (url=492ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-463MS` (url=819ms, status=HTTP 204)
25. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-497MS` (url=1254ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
