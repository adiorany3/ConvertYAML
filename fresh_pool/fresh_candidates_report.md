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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=218ms, nekobox=255ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=214ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=217ms, nekobox=246ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-73MS` (url=218ms, nekobox=243ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-74MS` (url=216ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=210ms, nekobox=243ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-92MS` (url=235ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-93MS` (url=222ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=221ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, nekobox=252ms, status=yes)
11. `AKUN-011-EU-VLESS-WS-84MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-114MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-101MS` (url=214ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-150MS` (url=316ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-97MS` (url=224ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-133MS` (url=339ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-154MS` (url=276ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-171MS` (url=378ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-142MS` (url=327ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-392MS` (url=625ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-412MS` (url=880ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-381MS` (url=617ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-418MS` (url=716ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-432MS` (url=732ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
