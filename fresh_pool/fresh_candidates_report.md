# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 13
- Kandidat strict NekoBox-tested: 6
- Proxy di openclash_fresh_pool.yaml: 19

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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=214ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=194ms, nekobox=178ms, status=no)
3. `AKUN-004-SPEEDTEST-VLESS-WS-119MS` (url=228ms, nekobox=173ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-334MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-373MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-388MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-353MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-434MS`
9. `AKUN-016-UNKNOWN-VLESS-WS-640MS` (url=932ms, nekobox=725ms, status=no)
10. `AKUN-023-UNKNOWN-VLESS-WS-625MS` (url=865ms, nekobox=750ms, status=no)
11. `AKUN-026-UNKNOWN-VLESS-WS-611MS` (url=877ms, nekobox=728ms, status=no)
12. `AKUN-027-UNKNOWN-VLESS-WS-619MS` (url=860ms, nekobox=766ms, status=no)
13. `AKUN-028-UNKNOWN-VLESS-WS-663MS` (url=915ms, nekobox=726ms, status=no)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
