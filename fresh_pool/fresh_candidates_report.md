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
1. `AKUN-001-ORACLE-VLESS-WS-63MS` (url=206ms, nekobox=236ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=213ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-70MS` (url=205ms, nekobox=250ms, status=yes)
4. `AKUN-004-U1HOST-FRA-VLESS-WS-70MS` (url=219ms, nekobox=246ms, status=yes)
5. `AKUN-005-HOSTOFF-NET-VLESS-WS-75MS` (url=231ms, nekobox=246ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=232ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-68MS` (url=213ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=212ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=219ms, nekobox=181ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-105MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-136MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-71MS` (url=197ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-80MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-247MS` (url=559ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-249MS` (url=561ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=550ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-241MS` (url=486ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-251MS` (url=487ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-237MS` (url=493ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-76MS` (url=222ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-369MS` (url=591ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-250MS` (url=536ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
