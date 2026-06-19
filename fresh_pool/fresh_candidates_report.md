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
1. `AKUN-001-ALIBABA-VLESS-WS-65MS` (url=200ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=212ms, nekobox=246ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=212ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDWEBMANAGE-EU-FR-VLESS-WS-73MS` (url=198ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=215ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, nekobox=234ms, status=yes)
8. `AKUN-008-EU-VLESS-WS-76MS` (url=215ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=247ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-71MS` (url=227ms, nekobox=230ms, status=no)
11. `AKUN-011-UNKNOWN-VLESS-WS-73MS` (url=198ms, nekobox=200ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=197ms, status=no)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, nekobox=220ms, status=no)
14. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-119MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-126MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-161MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-88MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-82MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-281MS` (url=557ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-262MS` (url=632ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-255MS` (url=556ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-374MS` (url=626ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
