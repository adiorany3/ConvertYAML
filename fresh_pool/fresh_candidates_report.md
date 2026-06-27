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
1. `AKUN-001-090227-VLESS-WS-77MS` (url=204ms, nekobox=268ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-79MS` (url=232ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=223ms, nekobox=239ms, status=no)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=205ms, nekobox=206ms, status=no)
5. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS`
12. `AKUN-010-CLOUDWEBMANAGE-EU-FR-VLESS-WS-107MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-114MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-120MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-229MS` (url=401ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-101MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-364MS` (url=731ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-392MS` (url=743ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-406MS` (url=870ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-400MS` (url=847ms, status=HTTP 204)
23. `AKUN-023-OCTOPUSSS5-VLESS-WS-417MS` (url=816ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-391MS` (url=820ms, status=HTTP 204)
25. `AKUN-025-SPEEDTEST-VLESS-WS-385MS` (url=836ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
