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
1. `AKUN-001-GOV-VLESS-WS-97MS` (url=323ms, nekobox=340ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=329ms, nekobox=370ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-98MS` (url=349ms, nekobox=365ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-94MS` (url=283ms, nekobox=339ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS` (url=318ms, nekobox=357ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=346ms, nekobox=356ms, status=yes)
7. `AKUN-007-HETZNER-VLESS-WS-116MS` (url=273ms, nekobox=393ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=294ms, nekobox=366ms, status=yes)
9. `AKUN-009-466688-VLESS-WS-113MS` (url=340ms, nekobox=335ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-103MS` (url=357ms, nekobox=329ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-100MS` (url=278ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=282ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-117MS` (url=291ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=343ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=332ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-117MS` (url=373ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-122MS` (url=329ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=293ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-117MS` (url=302ms, status=HTTP 204)
20. `AKUN-020-HETZNER-VLESS-WS-146MS` (url=371ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-133MS` (url=458ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-316MS` (url=676ms, status=HTTP 204)
23. `AKUN-023-INTERNETWORKS-45-131-210-VLESS-WS-317MS` (url=652ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-296MS` (url=673ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-309MS` (url=641ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
