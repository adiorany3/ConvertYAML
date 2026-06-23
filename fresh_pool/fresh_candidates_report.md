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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=235ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-113MS` (url=249ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS` (url=257ms, nekobox=264ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=233ms, nekobox=273ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-135MS` (url=242ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-127MS`
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS`
8. `AKUN-009-UNKNOWN-VLESS-WS-128MS` (url=292ms, nekobox=212ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-129MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-102MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-121MS`
12. `AKUN-015-CLOUDWEBMANAGE-EU-FR-VLESS-WS-140MS` (url=257ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-126MS` (url=261ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-126MS` (url=213ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-127MS` (url=247ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-383MS` (url=742ms, status=HTTP 204)
17. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-388MS` (url=869ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-438MS` (url=848ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-126MS` (url=240ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-441MS` (url=871ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-115MS` (url=230ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-417MS` (url=757ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-450MS` (url=849ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-173MS` (url=237ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-467MS` (url=800ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
