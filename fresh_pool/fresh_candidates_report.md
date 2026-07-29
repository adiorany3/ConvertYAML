# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-55MS` (url=218ms, nekobox=230ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-55MS` (url=223ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=229ms, nekobox=229ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=209ms, nekobox=244ms, status=yes)
6. `AKUN-006-HOSTINGER-VLESS-WS-71MS` (url=210ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=238ms, nekobox=303ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=240ms, nekobox=267ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS`
10. `AKUN-010-ZOOM-VLESS-WS-86MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-124MS` (url=235ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-145MS` (url=241ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-110MS` (url=333ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-110MS` (url=255ms, status=HTTP 204)
15. `AKUN-017-DEV-VLESS-WS-73MS` (url=845ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=210ms, status=HTTP 204)
17. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-387MS` (url=3787ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-156MS` (url=225ms, status=HTTP 204)
19. `AKUN-027-CLOUDFLARE-VLESS-WS-770MS` (url=4114ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-762MS` (url=3832ms, status=HTTP 204)
21. `AKUN-029-UNKNOWN-VLESS-WS-815MS` (url=797ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-626MS` (url=1420ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-569MS` (url=5545ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
