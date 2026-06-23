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
1. `AKUN-001-VULTR-VLESS-WS-60MS` (url=227ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=205ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=180ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-80MS`
6. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-87MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=220ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=224ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-180MS` (url=263ms, status=HTTP 204)
15. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=214ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-256MS` (url=582ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-253MS` (url=504ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-249MS` (url=534ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-278MS` (url=585ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, status=HTTP 204)
21. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-267MS` (url=562ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-73MS` (url=217ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-269MS` (url=503ms, status=HTTP 204)
24. `AKUN-028-OPENAI-VLESS-WS-78MS` (url=214ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-406MS` (url=643ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
