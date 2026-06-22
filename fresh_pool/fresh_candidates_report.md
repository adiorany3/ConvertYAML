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
1. `AKUN-001-VULTR-VLESS-WS-92MS` (url=223ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-103MS` (url=222ms, nekobox=231ms, status=no)
3. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-107MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS`
6. `AKUN-005-VULTR-VLESS-WS-97MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-125MS` (url=217ms, nekobox=228ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=199ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=338ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-370MS` (url=782ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-364MS` (url=792ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-402MS` (url=797ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-424MS` (url=886ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-434MS` (url=879ms, status=HTTP 204)
20. `AKUN-022-KAWAII520-VLESS-WS-671MS` (url=1076ms, status=HTTP 204)
21. `AKUN-031-UNKNOWN-VLESS-WS-778MS` (url=1195ms, status=HTTP 204)
22. `AKUN-033-UNKNOWN-VLESS-WS-893MS` (url=1491ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-878MS` (url=1491ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
