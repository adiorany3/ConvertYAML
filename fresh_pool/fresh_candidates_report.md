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
1. `AKUN-001-UNKNOWN-VLESS-WS-72MS` (url=212ms, nekobox=252ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-64MS` (url=193ms, nekobox=243ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=196ms, nekobox=268ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=246ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-85MS` (url=228ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=196ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, nekobox=231ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-86MS` (url=380ms, nekobox=261ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-123MS` (url=216ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=214ms, nekobox=254ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-103MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-106MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-77MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-090227-VLESS-WS-78MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-124MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-172MS` (url=371ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=207ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-350MS` (url=773ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-348MS` (url=743ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-379MS` (url=845ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-389MS` (url=826ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-406MS` (url=853ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-420MS` (url=905ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
