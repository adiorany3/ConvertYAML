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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=207ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-99MS` (url=214ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=209ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-105MS` (url=238ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=213ms, nekobox=250ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=228ms, nekobox=230ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-101MS` (url=215ms, nekobox=248ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS` (url=206ms, nekobox=252ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-103MS` (url=225ms, nekobox=238ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-122MS` (url=222ms, nekobox=251ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-113MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-139MS` (url=213ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-247MS` (url=519ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-261MS` (url=1681ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-260MS` (url=557ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-301MS` (url=582ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-283MS` (url=582ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-295MS` (url=641ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-311MS` (url=550ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-286MS` (url=615ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-272MS` (url=851ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-461MS` (url=763ms, status=HTTP 204)
24. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-528MS` (url=894ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-586MS` (url=844ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
