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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=242ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-94MS` (url=220ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=204ms, nekobox=238ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-97MS` (url=218ms, nekobox=247ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-87MS` (url=220ms, nekobox=242ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-111MS` (url=225ms, nekobox=242ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-101MS` (url=201ms, nekobox=256ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-89MS` (url=226ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=209ms, nekobox=242ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-78MS` (url=223ms, status=HTTP 204)
12. `AKUN-013-DEV-VLESS-WS-225MS` (url=995ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=236ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-246MS` (url=506ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-264MS` (url=595ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-233MS` (url=497ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-264MS` (url=564ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-271MS` (url=571ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-244MS` (url=989ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-271MS` (url=571ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-282MS` (url=615ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-506MS` (url=845ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-555MS` (url=823ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-492MS` (url=719ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
