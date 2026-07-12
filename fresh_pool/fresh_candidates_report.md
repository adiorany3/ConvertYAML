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
1. `AKUN-001-090227-VLESS-WS-61MS` (url=237ms, nekobox=242ms, status=yes)
2. `AKUN-002-CNAE-VLESS-WS-60MS` (url=226ms, nekobox=242ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-57MS` (url=222ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, nekobox=266ms, status=yes)
5. `AKUN-005-UDACITY-VLESS-WS-79MS` (url=253ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=228ms, nekobox=249ms, status=yes)
7. `AKUN-007-DE-XTOM-20190821-VLESS-WS-82MS` (url=321ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=237ms, nekobox=242ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS` (url=235ms, nekobox=291ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-67MS` (url=221ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-92MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-107MS` (url=248ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=244ms, status=HTTP 204)
14. `AKUN-014-DE-XTOM-20190821-VLESS-WS-80MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=242ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-134MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-194MS` (url=324ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-352MS` (url=754ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-369MS` (url=732ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-369MS` (url=775ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-388MS` (url=900ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-644MS` (url=1063ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-679MS` (url=1557ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
