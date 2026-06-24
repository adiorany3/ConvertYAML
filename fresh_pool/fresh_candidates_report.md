# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-136MS` (url=281ms, nekobox=286ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-129MS` (url=279ms, nekobox=297ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-136MS` (url=267ms, nekobox=326ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-151MS` (url=277ms, nekobox=301ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-134MS` (url=276ms, nekobox=313ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-155MS` (url=268ms, nekobox=340ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-165MS` (url=316ms, nekobox=342ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-148MS` (url=272ms, nekobox=228ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-145MS` (url=271ms, nekobox=245ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-155MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-141MS` (url=242ms, nekobox=232ms, status=no)
12. `AKUN-009-HCAPTCHA-VLESS-WS-140MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-379MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-386MS` (url=793ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-400MS` (url=746ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-407MS` (url=764ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-384MS` (url=791ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-148MS` (url=275ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-366MS` (url=749ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-381MS` (url=716ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-649MS` (url=1112ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-706MS` (url=976ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-760MS` (url=1135ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-816MS` (url=1057ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
