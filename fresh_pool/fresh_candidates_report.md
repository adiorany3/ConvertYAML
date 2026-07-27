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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-AIMALL-VLESS-WS-79MS` (url=346ms, nekobox=399ms, status=yes)
2. `AKUN-003-SPEEDTEST-VLESS-WS-89MS` (url=291ms, nekobox=190ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-99MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS`
5. `AKUN-007-SPEEDTEST-VLESS-WS-101MS` (url=290ms, nekobox=195ms, status=no)
6. `AKUN-008-SPEEDTEST-VLESS-WS-132MS` (url=331ms, nekobox=193ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-114MS`
8. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=267ms, nekobox=7178ms, status=no)
9. `AKUN-005-CLOUDFLARE-VLESS-WS-159MS`
10. `AKUN-006-CLOUDFLARE-VLESS-WS-189MS`
11. `AKUN-007-CLOUDFLARE-VLESS-WS-181MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-283MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-284MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-268MS`
15. `AKUN-017-CLOUDFLARE-VLESS-WS-326MS` (url=656ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-323MS` (url=655ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-117MS` (url=358ms, status=HTTP 204)
18. `AKUN-022-DEV-VLESS-WS-93MS` (url=648ms, status=HTTP 204)
19. `AKUN-023-SPEEDTEST-VLESS-WS-109MS` (url=388ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-139MS` (url=314ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-543MS` (url=887ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-139MS` (url=311ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-609MS` (url=1004ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-594MS` (url=1029ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-607MS` (url=1135ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
