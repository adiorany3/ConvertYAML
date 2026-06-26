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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=200ms, nekobox=227ms, status=yes)
2. `AKUN-002-MYBB-VLESS-WS-77MS` (url=238ms, nekobox=260ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-64MS` (url=226ms, nekobox=228ms, status=yes)
4. `AKUN-004-ORACLE-VLESS-WS-71MS` (url=226ms, nekobox=228ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=222ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=266ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=220ms, nekobox=246ms, status=yes)
8. `AKUN-008-1PASSWORD-VLESS-WS-86MS` (url=217ms, nekobox=252ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-129MS` (url=647ms, nekobox=560ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-97MS` (url=211ms, nekobox=244ms, status=yes)
11. `AKUN-011-SPACECORE-VLESS-WS-93MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-116MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-147MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-147MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-HOSTOFF-NET-VLESS-WS-115MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=271ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-391MS` (url=928ms, status=HTTP 204)
19. `AKUN-019-CONFLU-VLESS-WS-358MS` (url=721ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-334MS` (url=640ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-400MS` (url=868ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-386MS` (url=892ms, status=HTTP 204)
23. `AKUN-023-OCTOPUSSS5-VLESS-WS-408MS` (url=809ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-365MS` (url=781ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-361MS` (url=1390ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
