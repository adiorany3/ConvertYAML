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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=216ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS`
6. `AKUN-006-008500-VLESS-WS-96MS`
7. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-82MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS`
10. `AKUN-010-MEDIUM-VLESS-WS-82MS`
11. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS` (url=223ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-95MS` (url=225ms, status=HTTP 204)
13. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-154MS` (url=223ms, status=HTTP 204)
14. `AKUN-015-MYBB-VLESS-WS-80MS` (url=235ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-215MS` (url=375ms, status=HTTP 204)
16. `AKUN-017-ADF-VLESS-WS-86MS` (url=237ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-352MS` (url=750ms, status=HTTP 204)
18. `AKUN-019-CONFLU-VLESS-WS-369MS` (url=759ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-402MS` (url=2238ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-403MS` (url=879ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-396MS` (url=838ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-92MS` (url=228ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-430MS` (url=856ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-504MS` (url=1109ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-795MS` (url=1397ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
