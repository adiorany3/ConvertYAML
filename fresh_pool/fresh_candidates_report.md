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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=208ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=214ms, nekobox=245ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=209ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=217ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=226ms, nekobox=179ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS`
7. `AKUN-006-008500-VLESS-WS-99MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=222ms, nekobox=178ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-DIGITALOCEAN-VLESS-WS-107MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-CLOUDWEBMANAGE-EU-FR-VLESS-WS-98MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-84MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-93MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-83MS` (url=246ms, status=HTTP 204)
19. `AKUN-019-NETCUP-VLESS-WS-91MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-NET-NL-VLESS-WS-109MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-108MS` (url=213ms, status=HTTP 204)
23. `AKUN-023-SPACECORE-VLESS-WS-85MS` (url=233ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-93MS` (url=223ms, status=HTTP 204)
25. `AKUN-025-CONFLU-VLESS-WS-230MS` (url=487ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
