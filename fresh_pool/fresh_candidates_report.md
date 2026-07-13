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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=270ms, nekobox=191ms, status=no)
2. `AKUN-001-ZVC-VLESS-WS-77MS`
3. `AKUN-002-ZOOM-VLESS-WS-72MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=222ms, nekobox=7179ms, status=no)
6. `AKUN-004-UNKNOWN-VLESS-WS-73MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=259ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=250ms, nekobox=217ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-125MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-128MS` (url=254ms, nekobox=189ms, status=no)
14. `AKUN-010-CLOUDFLARE-VLESS-WS-257MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-268MS` (url=549ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-253MS` (url=466ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-287MS` (url=584ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-290MS` (url=638ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-204MS` (url=498ms, status=HTTP 204)
20. `AKUN-020-ES-FORNEX-20160629-VLESS-WS-92MS` (url=273ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-78MS` (url=534ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-369MS` (url=407ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-450MS` (url=994ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-465MS` (url=763ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-259MS` (url=551ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
