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
1. `AKUN-001-090227-VLESS-WS-73MS` (url=223ms, nekobox=258ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-64MS` (url=198ms, nekobox=184ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS`
6. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=203ms, nekobox=182ms, status=no)
9. `AKUN-007-UNKNOWN-VLESS-WS-90MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-351MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-366MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-385MS` (url=853ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-392MS` (url=885ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-358MS` (url=746ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-377MS` (url=829ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-410MS` (url=861ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-610MS` (url=892ms, status=HTTP 204)
19. `AKUN-026-BROADNNET-KR-VLESS-WS-684MS` (url=797ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-611MS` (url=883ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-548MS` (url=633ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-721MS` (url=2530ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-826MS` (url=1359ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
