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
1. `AKUN-001-ADF-VLESS-WS-108MS` (url=245ms, nekobox=347ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-101MS` (url=268ms, nekobox=388ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-101MS` (url=256ms, nekobox=339ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-108MS` (url=244ms, nekobox=352ms, status=yes)
5. `AKUN-005-HOSTOFF-NET-VLESS-WS-112MS`
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-113MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-136MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-138MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-136MS`
11. `AKUN-012-CLOUDWEBMANAGE-EU-FR-VLESS-WS-129MS` (url=260ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=346ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-148MS` (url=349ms, status=HTTP 204)
14. `AKUN-015-US-VLESS-WS-152MS` (url=252ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-128MS` (url=333ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-160MS` (url=340ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-157MS` (url=402ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-132MS` (url=379ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-166MS` (url=338ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-320MS` (url=697ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-348MS` (url=708ms, status=HTTP 204)
22. `AKUN-023-SPEEDTEST-VLESS-WS-376MS` (url=757ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-355MS` (url=745ms, status=HTTP 204)
24. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-363MS` (url=795ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-351MS` (url=718ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
