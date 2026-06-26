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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=236ms, nekobox=275ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=231ms, nekobox=261ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-85MS` (url=234ms, nekobox=256ms, status=yes)
4. `AKUN-004-NET-NL-VLESS-WS-85MS` (url=260ms, nekobox=259ms, status=yes)
5. `AKUN-005-NETCUP-VLESS-WS-69MS` (url=293ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=286ms, nekobox=300ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=224ms, nekobox=256ms, status=yes)
8. `AKUN-008-U1HOST-FRA-VLESS-WS-76MS` (url=259ms, nekobox=273ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, nekobox=184ms, status=no)
10. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-89MS`
11. `AKUN-010-DIGITALOCEAN-VLESS-WS-76MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-121MS` (url=288ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-77MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-67MS` (url=239ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-85MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-71MS` (url=249ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-102MS` (url=245ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=552ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-99MS` (url=238ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-293MS` (url=513ms, status=HTTP 204)
23. `AKUN-023-OCTOPUSSS5-VLESS-WS-293MS` (url=653ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-289MS` (url=615ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-296MS` (url=716ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
