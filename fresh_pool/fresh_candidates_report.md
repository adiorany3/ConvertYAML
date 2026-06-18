# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=195ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=211ms, nekobox=245ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-65MS` (url=203ms, nekobox=178ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=198ms, nekobox=191ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS`
7. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-89MS`
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, nekobox=198ms, status=no)
13. `AKUN-010-CLOUDWEBMANAGE-EU-FR-VLESS-WS-83MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-392MS` (url=846ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-385MS` (url=738ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-378MS` (url=751ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-415MS` (url=2426ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-378MS` (url=825ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-482MS` (url=859ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-410MS` (url=905ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-424MS` (url=876ms, status=HTTP 204)
22. `AKUN-031-ONTHEWIFI-VLESS-WS-795MS` (url=1213ms, status=HTTP 204)
23. `AKUN-033-US-VLESS-WS-536MS` (url=300ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-894MS` (url=1807ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
