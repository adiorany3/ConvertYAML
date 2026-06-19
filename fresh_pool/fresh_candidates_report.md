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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=236ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=205ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=229ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=937ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=232ms, nekobox=256ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-93MS` (url=222ms, nekobox=299ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=221ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=232ms, nekobox=182ms, status=no)
10. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-86MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-82MS` (url=228ms, nekobox=186ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-123MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-154MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-264MS` (url=599ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-244MS` (url=521ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-287MS` (url=930ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-278MS` (url=560ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-267MS` (url=4057ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-264MS` (url=554ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
