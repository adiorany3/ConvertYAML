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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=228ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=242ms, nekobox=183ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS`
5. `AKUN-004-VULTR-VLESS-WS-81MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
8. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-103MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=257ms, nekobox=205ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-83MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-118MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-85MS` (url=269ms, nekobox=180ms, status=no)
13. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=240ms, status=HTTP 204)
15. `AKUN-016-CLOUDWEBMANAGE-EU-FR-VLESS-WS-92MS` (url=249ms, status=HTTP 204)
16. `AKUN-017-CONFLU-VLESS-WS-266MS` (url=566ms, status=HTTP 204)
17. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-291MS` (url=646ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-277MS` (url=669ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-263MS` (url=554ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-305MS` (url=682ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-274MS` (url=576ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-327MS` (url=668ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-522MS` (url=789ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-102MS` (url=240ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-653MS` (url=1040ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
